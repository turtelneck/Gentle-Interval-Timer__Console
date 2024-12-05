tell application "System Events"
	set isSpotifyRunning to (exists (process "Spotify"))
	set isMusicRunning to (exists (process "Music"))
end tell

if isSpotifyRunning then
	tell application "Spotify"
		pause
		log "paused Spotify successfully!"
	end tell
else if isMusicRunning then
	tell application "Music"
		pause
		log "paused Music successfully!"
	end tell
else
	log "Neither Spotify nor Music is currently running."
end if
