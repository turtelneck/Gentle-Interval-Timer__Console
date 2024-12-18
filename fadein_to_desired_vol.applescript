on run {desiredVolume}
	
	set currentVolume to output volume of (get volume settings)
	set interval to (1 / 60 * minutes) -- fade-in interval, 1 second
	
	-- Avoid division by 0
	if desiredVolume is 0 then
		set waitTime to interval -- Assign a fallback wait time
	else
		set waitTime to interval / (desiredVolume - currentVolume) -- spread out over interval time
	end if
	
	-- gradually increase volume
	repeat with X from currentVolume to desiredVolume by 1
		set X to round (X) -- Ensure X is an integer
		set volume output volume X
		delay waitTime
	end repeat
	
end run
