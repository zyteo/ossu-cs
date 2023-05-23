;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 1a-booleans-and-if-part4) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

(define I1 (rectangle 10 20 "solid" "yellow"))
(define I2 (rectangle 20 10 "solid" "green"))

;other expressions


(and (> (image-height I1) (image-height I2))
     (< (image-width I1) (image-width I2)))

(or (> (image-height I1) (image-height I2))
     (< (image-height I1) (image-width I2)))