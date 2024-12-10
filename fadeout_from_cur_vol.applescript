on run
	
	set currentVolume to output volume of (get volume settings)
	set interval to (3 / 60 * minutes) -- 3 seconds
	set waitTime to interval / currentVolume
	
	-- gradually decrease volume
	repeat with X from currentVolume to 1 by -1
		set X to round (X) -- X must be integer
		set volume output volume X
		delay waitTime
	end repeat
	
	-- avoids divide by 0 during previous operations
	set volume output volume 0
	
	return currentVolume
	
end run
