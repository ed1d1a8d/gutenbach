-- -----------------
-- iTunes -> gutenbach
-- -----------------
-- This is a simple little script which sends
-- music from an iTunes library to the gutenbach
-- lpr server.
--
-- Changelog:
--
-- 23 Aug 2009 -> broder spun loop into shell script instead of
--     applescript so that iTunes doesn't hang
-- 9 Jan 2009 -> price added 'quoted form'
-- 7 Jan 2009 -> kmill created initial version
--
-- Installation:
--
-- 1) Launch the Printer Setup Utility and add
--    an IP Printer with the LPD protocol with
--    the following information:
--     Address: zygorthian-space-raiders.mit.edu
--     Queue: gutenbach
--    It is not necessary to specify the driver.
--
-- 2) Create the directory ~/Library/iTunes/Scripts
--    and place the "Send to gutenbach.scpt" file
--    within.
--
-- Usage:
--
-- When in iTunes, select the songs which you
-- would like to hear in the office, and click
-- "Send to gutenbach" in the script menu from
-- the menu bar.  The script menu looks like a
-- little scroll icon.  There will be no
-- feedback beyond the pleasant sounds you now
-- hear around you.

set ts to ""

tell application "iTunes"
	repeat with t in selection
		if class of t is (file track) then
			set loc to POSIX path of (get location of t)
			set ts to ts & " " & (quoted form of loc)
		end if
	end repeat
end tell

set command to "(for t in " & ts & "; do lpr -o raw -Pgutenbach \"$t\"; done) >/dev/null 2>&1 </dev/null &"
do shell script command
