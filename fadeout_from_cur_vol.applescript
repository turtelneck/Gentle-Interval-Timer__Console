on run
	
	set desiredVolume to 1 -- avoids divide by 0 when setting waitTime
	set currentVolume to output volume of (get volume settings)
	set interval to (1 / 20 * minutes) -- start to finish time
	set waitTime to interval / currentVolume -- spread out over interval time
	
	-- Gradually decrease volume
	repeat with X from currentVolume to desiredVolume by -1
		set X to round (X) -- Ensure X is an integer
		set volume output volume X
		delay waitTime
	end repeat
	
	set volume output volume 0 -- avoids divide by 0 when setting waitTime
	
	return currentVolume
	
end run
