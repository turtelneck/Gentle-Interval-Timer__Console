on run
	
	set currentVolume to output volume of (get volume settings)
	set volume output volume 0
	
	tell application "System Events"
		set isSpotifyRunning to (exists (process "Spotify"))
		set isMusicRunning to (exists (process "Music"))
	end tell
	
	if isSpotifyRunning then
		tell application "Spotify"
			play
			--log "resumed Spotify successfully!"
		end tell
	else if isMusicRunning then
		tell application "Music"
			play
			--log "resumed Music successfully!"
		end tell
	else
		log "Neither Spotify nor Music is currently running."
	end if
	
	return currentVolume
	
end run
