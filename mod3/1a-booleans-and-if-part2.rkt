;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 1a-booleans-and-if-part2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

(define I1 (rectangle 10 20 "solid" "yellow"))
(define I2 (rectangle 20 10 "solid" "green"))

;if expressions
(if (< (image-width I1)
      (image-height I1))
    "tall"
    "wide")

(if (< (image-width I2)
      (image-height I2))
    "tall"
    "wide")

