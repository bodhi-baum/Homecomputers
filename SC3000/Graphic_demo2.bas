50 REM Computer Input 11.83, page 27
100 REM ***DEMO 2 CIRCLE***
110 LPRINT CHR$(18)
120 PAI=3.14159:A=240
130 FOR L=0 TO 240 STEP 10
140 LPRINT "M"+STR$(240+L)+",-240"
150 FOR TH=0 TO 2*PAI STEP PAI/16
160 X=l*COS(TH)
170 Y=(A-L)*SIN(TH)
180 GX=240+X
190 GY=-240+Y
200 LPRINT "D"+STR$(GX)+","+STR$(GY)
210 NEXT H
220 NEXT L
230 LPRINT "A"
240 END