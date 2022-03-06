
%med 4 specialtecken och olika ordlängder
ordlangd=1:10;
ordkomb1=[14 40 91 176 304 484 725 1036 1426 1904];

%med ordet "fyra" och olika specialtecken
specialtecken=1:10;
ordkomb2=[66 121 176 231 286 341 396 451 506 561];

figure(1)
plot(ordlangd,ordkomb1,'b'), hold on
xlabel("Längd på ordet"),ylabel("Antalet kombinationer")
title("Konstant antal specialtecken")
plot(ordlangd,ordlangd.^3.3,'r'), hold off

figure(3)
loglog(ordlangd,ordkomb1)

figure(2)
plot(specialtecken,ordkomb2,'b'), hold on
xlabel("Antalet specialtecken")
ylabel("Antalet kominationer")
title("Konstant antal bokstäver i ord")
plot(specialtecken,57*specialtecken,'r'), hold off