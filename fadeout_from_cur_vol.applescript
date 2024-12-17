on run
	
	set currentVolume to output volume of (get volume settings)
	set interval to (3 / 60 * minutes) -- 3 seconds

	-- Avoid division by 0
	if currentVolume is 0 then
		set waitTime to interval -- Assign a fallback wait time
	else
		set waitTime to interval / currentVolume
	end if
	
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
