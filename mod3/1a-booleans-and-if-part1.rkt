;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 1a-booleans-and-if-part1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
;true
;false

(define WIDTH 100)
(define HEIGHT 100)

(> WIDTH HEIGHT)
(>= WIDTH HEIGHT)

(= 1 2)
(= 1 1)
(> 3 9)

(string=? "boo" "bar")

(define I1 (rectangle 10 20 "solid" "yellow"))
(define I2 (rectangle 20 10 "solid" "green"))

(< (image-width I1)
   (image-width I2))
