on run {desiredVolume}
	
	set currentVolume to output volume of (get volume settings)
	set interval to (1 / 60 * minutes) -- start to finish time
	set waitTime to interval / (desiredVolume - currentVolume) -- spread out over interval time
	
	-- Gradually increase volume
	repeat with X from currentVolume to desiredVolume by 1
		set X to round (X) -- Ensure X is an integer
		set volume output volume X
		delay waitTime
	end repeat
	
end run
