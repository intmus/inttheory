\version "2.14.2"

#(set-default-paper-size "letter")
#(set-global-staff-size 20)

\header {
    title = ""
	subtitle = ""
	poet = ""
	composer = ""
	tagline = ""
	copyright = ""
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
	
	 	indent = 0.1\in
		top-margin = 0.5\in
		bottom-margin = 0.25\in
		line-width = 7.0\in
		ragged-right = ##f
		ragged-bottom = ##f
		ragged-last-bottom = ##t
		system-system-spacing #'minimum-distance = #20
		markup-system-spacing #'minimum-distance = #15
		score-system-spacing #'minimum-distance = #25
		last-bottom-spacing #'minimum-distance = #15
		%	page-count = #3
		print-page-number = ##f
	
	}

global = { 
	\override Score.PaperColumn #'keep-inside-line = ##t 	
	\override Staff.TimeSignature #'style = #'() 
	\override Staff.KeyCancellation #'break-visibility = #all-invisible
	\override Staff.TimeSignature #'break-visibility = #end-of-line-invisible
	\set Staff.explicitKeySignatureVisibility = #end-of-line-invisible
	\set Staff.explicitClefVisibility = #end-of-line-invisible	

	% enter key signature, time signature, pickup length here
%	\partial 8
	}

upper = <<
	\new Voice = "upper" <<
		\relative c'' {
            \clef treble
            \key b \minor \time 2/2 
        <<
            {
                d2 e fis e d cis b1 \bar "|." \break
            } \\
            {
                <fis b>2 <g b> <fis b> <fis ais> <fis b> <e ais> <d fis>1
            }
        >>

            \key bes \major \time 2/2 
        <<
            {
                d'2 c bes bes bes a bes1 \bar "|." \break
            } \\
            {
                <f bes>2 <f a> <f bes> es <d f> <c es> <bes d>1
            }
        >>

            \key b \minor \time 2/2 
        <<
            {
                d'2 e fis e d cis b1 \bar "|." \break
            } \\
            {
                <fis b>2 <g b> <fis b> <fis ais> <fis b> <e ais> <d fis>1
            }
        >>

            \key bes \major \time 2/2 
        <<
            {
                d'2 c bes bes bes a bes1 \bar "|." \break
            } \\
            {
                <f bes>2 <f a> <f bes> es <d f> <c es> <bes d>1
            }
        >>

        \key c \minor \time 2/2 
    <<
        {
            g''2 aes g g f4 es d2 c1 \bar "|." \break
        } \\
        {
            <c es>2 <c f> <b d> c <aes c> <g b> <es g>1
        }
    >>

	}

		>>
	>>

lower = <<
	\new Voice = "bass" <<
		\figuremode {
			\bassFigureStaffAlignmentUp
			\override BassFigure #'extra-offset = #'(0 . 1)
			

			% enter figures here within <> brackets
				% use + for sharp, - for flat, ! for natural
				% _ will make accidental by itself (apply to 3)
				% use s if bass note has no figure
		    s2 <6> <6> <6/ 4 3> s <7 _+> s1
	        s2 <4 2> <6> <6> <8 6 4> <7 5 3> s1
		    s2 <6> <6> <6/ 4 3> s <7 _+> s1
	        s2 <4 2> <6> <6> <8 6 4> <7 5 3> s1
			s2 s <4/ 2> <6> s <_!> s1
			}

		\relative c {
            \clef bass
            \key b \minor
            b'2 g d cis b fis' b,1 \bar "|." \break
            
            \key bes \major
            bes2 es d g f f, bes1 \bar "|." \break

            \key b \minor
            b'2 g d cis b fis' b,1 \bar "|." \break
            
            \key bes \major
            bes2 es d g f f, bes1 \bar "|." \break
			
			\key c \minor
			c2 f f es f g c,1
            
			}		
		>>
	>>

functionalBass = {
	\set stanza = \markup { \normal-text "" }
		\lyricmode {

		% enter functional bass here, follwing the rules of lilypond lyrics
        \skip2 \skip2 \skip2 \skip2 \skip2 \skip2 \skip2 
		\skip2 \skip2 \skip2 \skip2 \skip2 \skip2 \skip2 
        "T(1" "S6d" "3" "D2p" "1)" "D5" "T1"
        "T1" "D4" "T3" "S6" "D5" "—" "T1"
		}
	}

roman = {
	\set stanza = \markup { \normal-text "" }
		\lyricmode {
	
		% enter functional bass here, follwing the rules of lilypond lyrics
        I IV I V I V I
        I V I IV V "—" I
        \skip2 \skip2 \skip2 \skip2 \skip2 \skip2 \skip2 
		\skip2 \skip2 \skip2 \skip2 \skip2 \skip2 \skip2 
		i iv V i iv V i
		}
	}

functions = {
	\set stanza = \markup { \normal-text "" }
		\lyricmode {

		% enter functional bass here, follwing the rules of lilypond lyrics
        T S T D T D T
		T "—" "—" S D "—" T
		\skip2 \skip2 \skip2 \skip2 \skip2 \skip2 \skip2 
		T "—" "—" S D "—" T
		T "—" "—" "—" S D T
	}
	}

\score {
	\new PianoStaff \with { 
		\override StaffGrouper #'staff-staff-spacing #'minimum-distance = #15
		}
		<<
		\new Staff = "Staff_pfUpper" << \global \upper >>
		\new Staff = "Staff_pfLower" << \global \lower >>
		\new Lyrics \lyricsto "bass" { \roman }
		\new Lyrics \lyricsto "bass" { \functions }
	\new Lyrics \lyricsto "bass" { \functionalBass }
		>>
	\layout { 
		\context { \Score \remove "Bar_number_engraver" }
%		\context { \Staff \remove "Time_signature_engraver" }
		}
%  	\midi { }
	}
