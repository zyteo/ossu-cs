;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 2-itemization-part3) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Data definitions
;TLight is one of
;-false
;-red
;-yellow
;-green
;interpretation false means disabled, otherwise, colour of lights

(define TL1 false)
(define TL2 "red")

(define (fn-for-tlight tl)
  (cond [(false? tl) (...)]
        [(string=? tl "red") (...)]
        [(string=? tl "yellow") (...)]
        [(string=? tl "green") (...)]))

;template rules used:
;one of 4 cases:
;atomic distinct: false
;atomic distinct: "red"
;atomic distinct: "yellow"
;atomic distinct: "green"