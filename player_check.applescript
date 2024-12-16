on run
	
	set isSpotifyPlaying to false
	set isMusicPlaying to false
	
	tell application "System Events"
		if (exists (process "Spotify")) then
			tell application "Spotify"
				set isSpotifyPlaying to (player state is playing)
				log isSpotifyPlaying
			end tell
		end if
		if (exists (process "Music")) then
			tell application "Music"
				set isMusicPlaying to (player state is playing)
				log isMusicPlaying
			end tell
		end if
	end tell
	
	return (isSpotifyPlaying or isMusicPlaying)
	
end run