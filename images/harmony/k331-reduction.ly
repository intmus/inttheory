\version "2.18.2" 
#(set-default-paper-size "letter")
#(set-global-staff-size 20)

\header {
title = \markup { \smallCaps { "" } }
subtitle = \markup { \smallCaps { "" } }
composer = ""
poet = ""
tagline = ""
}

\paper {
	myStaffSize = #20
	#(define fonts
   (make-pango-font-tree  "Fanwood"
                          "Nimbus Sans"
                          "Luxi Mono"
;;                        "Helvetica"
;;                        "Courier"
     (/ myStaffSize 20)))
	
 	indent = 0.75\in
 	top-margin = 0.5\in
 	bottom-margin = 0.25\in
 	page-top-space = 1\in
 	before-title-space = 0\in
 	between-title-space = 1.5\in
 	line-width = 7.5\in
 	left-margin = 0.5\in
 	right-margin = 0.5\in
 	ragged-right = ##f
 	ragged-bottom = ##t
 	ragged-last-bottom = ##t
	%top-markup-spacing #'minimum-distance = #25
	system-system-spacing #'minimum-distance = #20
	markup-system-spacing #'minimum-distance = #20
	score-system-spacing #'minimum-distance = #18
	last-bottom-spacing #'minimum-distance = #15
	%	page-count = #3
	print-page-number = ##f
	
}

global = { 
	\override Score.PaperColumn #'keep-inside-line = ##t 	
	\override Score.BarNumber #'padding = #2
	\override Staff.TimeSignature #'style = #'() 
	\set majorSevenSymbol = \markup { "maj7" }
	\set Staff.printKeyCancellation = ##f 
	\override Staff.TimeSignature #'break-visibility = #end-of-line-invisible
	\set Staff.explicitKeySignatureVisibility = #end-of-line-invisible
	\set Staff.explicitClefVisibility = #end-of-line-invisible	

	% enter key signature, time signature, pickup length here
	\key a \major
	\time 6/8
%	\partial 8
	}

lyricsGlobal = {
	\override Score.LyricText #'font-size = #1
	\set extendersOverRests = ##f
}

harmonies = \chordmode {
	\override ChordName #'font-family = #'roman
	\override ChordName #'font-size = #0.5
	\override ChordName #'Y-offset = #5
	\set majorSevenSymbol = \markup { "maj7" }
	
}

upper = \relative c'' {
	\override Score.RehearsalMark #'self-alignment-X = #LEFT
	\override Score.RehearsalMark #'self-alignment-Y = #2
	\override Score.RehearsalMark #'X-offset = #0
	\override Score.RehearsalMark #'font-size = #1
	\override Score.RehearsalMark #'padding = #5
	\clef treble
	\override TextScript #'Y-offset = #4
	cis8.(\p\< d16) cis8-. e4---.(\> e8-.)\!
	b8.( cis16\<) b8-. d4---.(\> d8-.)\!
	a4(---. a8-.)\< b4---.( b8---.)\!
	<< { cis4 e16( d) cis4( b8-.) } \\ { s4 b8 a4(\> gis8)\! } >>
	\bar "|"
    }

lower = \relative c' { 
	\clef bass
	<<
		{	e4 e8-. e4 e8
			e4 e8 e4 e8-.
			e4-.( e8-.) e4-.( e8-.)
			e4 } \\
		{	a,8.( b16) a8 cis4---.( cis8-.)
			gis8.( a16) gis8-. b4---.( b8-.)
			fis4 fis8 gis4 gis8
			a4
			}
		>>
		d,8 e4.
	}

TrebleStaff = <<
	\new Voice = "bass" <<
		\relative c'' {
			\clef treble
		
			% enter bass line here
            \key a \major
            <cis e>2.
			<b d>
			a4. b
			cis4 <b d>8 <a cis>4 <gis b>8
            \bar "|." \break
            			
		}
	
		>>
	>>

BassStaff = <<
	\figuremode {
		\bassFigureStaffAlignmentUp
		\override BassFigure #'extra-offset = #'(0 . 3)
		\bassFigureExtendersOff
		
		% enter figures here within <> brackets
			% use + for sharp, - for flat, ! for natural
			% _ will make accidental by itself (apply to 3)
			% use s if bass note has no figure
			s2. <6 5> <7>4. <6> s4 <6>8 <6 4>4 <5 3>8
		
		}

	\new Voice = "bass" <<
		\relative c' {
			\clef bass
			
			% enter bass line here
            \key a \major
			<a cis e>2.
			<gis b e>
			<fis e'>4. <gis e'>
			<a e'>4 d,8 e4.
			\bar "|." \break
            
		}
		
		>>
	>>

roman = {
	\set stanza = \markup { \normal-text "" }
		\lyricmode {
	
		% enter functional bass here, follwing the rules of lilypond lyrics
		\once \override LyricText.self-alignment-X = #1
		"A: I" "V" "vi" V I ii V
	}
	}

func = {
	\set stanza = \markup { \normal-text "" }
		\lyricmode {

		% enter functional bass here, follwing the rules of lilypond lyrics
		\once \override LyricText.self-alignment-X = #1
		T D T D T S D
	}
	}

funclower = {
	\set stanza = \markup { \normal-text "" }
		\lyricmode {

		% enter functional bass here, follwing the rules of lilypond lyrics
		\once \override LyricText.self-alignment-X = #1
		T \skip2 \skip2 \skip2 \skip2 S D
	}
	}

cadences = {
	\set stanza = \markup { \normal-text "" }
		\lyricmode {

		% enter functional bass here, follwing the rules of lilypond lyrics
		\once \override LyricText.self-alignment-X = #1
		\skip2 \skip2 \skip2 \skip2 \skip2 \skip2 HC
	}
	}


\score {
	<<
		\new ChordNames {
				\harmonies
				}
		\new PianoStaff \with { 
			\override StaffGrouper.staffgroup-staff-spacing.basic-distance = #12
			\override StaffGrouper #'staff-staff-spacing #'minimum-distance = #12
		}
			<<
			\set PianoStaff.instrumentName = "Original "
			\set PianoStaff.shortInstrumentName = " "
			\set PianoStaff.midiInstrument = "piano" 
			\new Staff = "Staff_pfUpper" << \global \upper >>
			\new Staff = "Staff_pfLower" << \global \lower >>
	%		\new Lyrics \lyricsto "bass" { \functionalBass }
	 %   	\new Lyrics \lyricsto "bass" { \functionalBassLower }
			>>
		\new PianoStaff \with { 
			\override StaffGrouper #'staff-staff-spacing #'minimum-distance = #12
			}
			<<
			\set PianoStaff.instrumentName = "Reduction "
			\set PianoStaff.shortInstrumentName = " "
			\set PianoStaff.midiInstrument = "piano" 
			\new Staff = "Staff_pfUpper" << \global \TrebleStaff >>
			\new Staff = "Staff_pfUpper" << \global \BassStaff >>
			\new Lyrics \with {
    \override VerticalAxisGroup.nonstaff-relatedstaff-spacing = #'((basic-distance . 7))
  }
				\lyricsto "bass" { \lyricsGlobal \roman }
		    	\new Lyrics \lyricsto "bass" { \func }
		    	\new Lyrics \lyricsto "bass" { \funclower }
		    	\new Lyrics \lyricsto "bass" { \cadences }
			>>
   >>
}

