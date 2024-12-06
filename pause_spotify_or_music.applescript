on run {prev_vol}
	
	set isSpotifyPlaying to false
	set isMusicPlaying to false
	
	tell application "System Events"
		if (exists (process "Spotify")) then
			tell application "Spotify"
				set isSpotifyPlaying to (player state is playing)
			end tell
		end if
		if (exists (process "Music")) then
			tell application "Music"
				set isMusicPlaying to (player state is playing)
			end tell
		end if
	end tell
	
	if isSpotifyPlaying then
		tell application "Spotify"
			pause
			-- log "paused Spotify successfully!"
		end tell
	end if
	if isMusicPlaying then
		tell application "Music"
			pause
			-- log "paused Music successfully!"
		end tell
	end if
	
	-- return volume to pre-fade levels
	set volume output volume prev_vol
	
	return (isSpotifyPlaying or isMusicPlaying)
	
end run
