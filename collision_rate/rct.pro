function lineoffile, filename
num = 0l
str = ''
openr, 10, filename
while ~eof(10) do begin
	readf, 10, str
	num++
endwhile
close, 10
return, num
end

function read_cr, file_name, n

n = lineoffile(file_name) - 1 ; first line is comment

struct_rct = {	id: 0l, $
				rad: 0.0d, $
				nd: 0.0d, $
				A: 0.0d, $
				v: 0.0d, $
				cr: 0.0d}

array = replicate(struct_rct, n)

str = ''
openr, 10, file_name
readf, 10, str
readf, 10, array
close, 10

return, array

end

; cr: collision rate

function calc_r_cr, n, rin, crin, nbin, range, rout, crout
	
	dr	=	range * 1.0d / nbin
	rout	=	(rout + 0.5) * dr
	
	count	=	lonarr(nbin)

	id = 0l

	for i = 0l, n - 1l do begin

		id = floor(rin(i) / dr)
		if id lt nbin then begin
			count(id)++
			crout(id) += crin(i)
		endif

	endfor

	crout /= count

	return, 0
end

pro rct, dir, file_num, rsize

!p.font			=	0
!p.thick		=	4
!p.charthick	=	1
!p.charsize		=	1.2
!p.symsize		=	1

red	= 249
green	=	250
blue      =   251
deepred   =   252
deepblue  =   253
purple    =   254
dotted    =   1
dash      =   2
tvlct, 0, 255, 0, green
tvlct,255,0,0,red
tvlct,189,0,95,deepred
tvlct,0,0,255,blue
tvlct,0,0,127,deepblue
tvlct,255,0,255,purple

Myr		=	3.1556926D13
Msol	=	1.98892D30
km		=	1.0e3

R_gas	=	8.31447215
MJU		=	1.3e-3

TNORM	=	1.4881311975633394D14
MNORM	=	1.98892D40

dir_base = '~/program/mp-cd-sph/run'
file_name = dir_base + '/' + dir + '/cr' + file_num + '.dat'

ntot = 0l

array = read_cr(file_name, ntot)

nbin = 25
rout = dindgen(nbin)
crout = dblarr(nbin)
	
result = calc_r_cr(ntot, array.rad, array.cr, nbin, rsize, rout, crout)

eps_name = 'r-ct-' + dir + '-' + file_num + '.eps'

set_plot, 'ps'
device, /encapsul, filename = eps_name, /color

ytit = 'Collision Time Scale [Myr]'

plot, rout, 1.0 / crout, xrange = [0, rsize], yrange = [1.0, 10.0^8], $
		xstyle = 1, ystyle = 1, linestyle = 0, $
		xtitle = 'Radius [kpc]', ytitle = ytit, $
		/ylog

device, /close_file
set_plot, 'x'

;;;;;;;;;;;;;;;;;;;; r - v_disp ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

nbin = 25
rout = dindgen(nbin)
vout = dblarr(nbin)
	
result = calc_r_cr(ntot, array.rad, array.v, nbin, rsize, rout, vout)

eps_name = 'r-vdisp-' + dir + '-' + file_num + '.eps'

set_plot, 'ps'
device, /encapsul, filename = eps_name, /color

ytit = 'Velocity Dispersion [km/s]'

plot, rout, vout, xrange = [0, rsize], yrange = [0.0, 80.0], $
		xstyle = 1, ystyle = 1, linestyle = 0, $
		xtitle = 'Radius [kpc]', ytitle = ytit

device, /close_file
set_plot, 'x'

end
