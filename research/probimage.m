width = 2;
height = 1;

freqA = 400;
freqB = 500;
phaseA = 0.0;
phaseB = 0.0;

locA = [0,0];
locB = [0,1];

speedOfSound = 343;

imRes = 100;

image = ones(width*imRes, height*imRes);

for phaseB = 0:.1:1

	for x = 1:width*imRes
		for y = 1:height*imRes
			distA = sqrt((locA(1) - x/imRes)^2+(locA(2) - y/imRes)^2);
			distB = sqrt((locB(1) - x/imRes)^2+(locB(2) - y/imRes)^2);
			image(x,y) = cos(pi*(freqA*distA/speedOfSound - phaseA))^8 * ...
				cos(pi*(freqB*distB/speedOfSound - phaseB))^8;
		end
	end

	imshow(image');
end