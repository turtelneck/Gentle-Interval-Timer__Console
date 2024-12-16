on run {prev_vol}
	
	tell application "System Events"
		if (exists (process "Spotify")) then
			tell application "Spotify"
				pause
			end tell
		end if
		if (exists (process "Music")) then
			tell application "Music"
				pause
			end tell
		end if
	end tell
	
	-- return volume to pre-fade levels
	set volume output volume prev_vol
	
end run
