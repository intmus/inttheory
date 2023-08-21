\version "2.18.2"

#(set-default-paper-size "letter")
#(set-global-staff-size 20)

\header {
	title = "post-tonal collections"
	subtitle = ""
	poet = ""
	composer = ""
	tagline = ""
	copyright = ""
	}

\paper {
	indent = 0.0\in
	top-margin = 0.5\in
	bottom-margin = 0.25\in
	page-top-space = 0\in
	before-title-space = 0\in
	between-title-space = 1.5\in
	after-title-space = 1.05\in
	line-width = 7.0\in
	left-margin = 0.75\in
	right-margin = 0.75\in
	ragged-right = ##t
	ragged-bottom = ##f
	ragged-last-bottom = ##t
	system-system-spacing #'minimum-distance = #15
	markup-system-spacing #'minimum-distance = #18
	last-bottom-spacing #'minimum-distance = #15
%	page-count = #3
	print-page-number = ##f
	}

global = { 
	\override Score.PaperColumn #'keep-inside-line = ##t 	
	\override Score.BarNumber #'padding = #2
	\override VoltaBracket #'extra-offset = #'(0 . -3)
	\override ChordName #'font-family = #'roman
	\override Score.LyricText #'font-series = #'bold
	\override Score.LyricText #'font-family = #'sans
	\override ChordName #'font-size = #0.5
	\override Staff.TimeSignature #'style = #'() 
	\set majorSevenSymbol = \markup { "maj7" }
	\override Staff.StaffGrouper #'staff-staff-spacing #'minimum-distance = #40

	% enter key signature, time signature, pickup length here
	\key c \major
	\time 2/2
%	\partial 8
	}

lower = <<
	\new Voice = "bass" <<
		\relative c' {
			\clef treble
			\time 8/1 
            c1 d e f g a b c \bar "|." \break
			
			d, e f g a b c d \bar "|." \break
			
			e, f g a b c d e \bar "|." \break
			
			f, g a b c d e f \bar "|." \break
			
			g, a b c d e f g \bar "|." \break
            
            a, b c d e f g a \bar "|." \break
			
			b, c d e f g a b \bar "|." \break
            
            \time 6/1
            ges, aes bes des es ges \bar "|." \break
            
            c,, d e g a c \bar "|." \break
            
            \time 9/1
            c, des es e! fis g a bes c \bar "|." \break
            
            \time 7/1
            c, dis e g aes b c \bar "|." \break
            
            \time 4/1 
            c,1 des d es \bar "|." \break
            
            c1 d e fis \bar "|." \break
            
            c des ges g! \bar "|." \break
            
            c, d fis gis \bar "|." \break
            
            \time 7/1
            c, d e fis gis ais c \bar "|." \break
            
            \time 8/1
            c, d e fis g a bes c \bar "|." \break
            
            \time 9/1
            c, d e f fis g a b c \bar "|." \break
            
            c, d e f g a bes b c \bar "|." \break
			}
		
		>>
	>>

\score {
	<<
		\new Staff = "Staff_pfLower" << \global \lower >>
		>>
    	\layout { 
    		\context { \Score \remove "Bar_number_engraver" }
    		\context { \Staff \remove "Time_signature_engraver" }
    		}
	}
