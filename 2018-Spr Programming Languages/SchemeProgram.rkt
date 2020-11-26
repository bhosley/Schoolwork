(define has-target-num?
  (lambda (Sum Set)
    (if (member Sum Set) (display #t) (display ""))))

(define (has-subtarget? Lst SubA SubB Holder)
    (cond
      ((eqv? Holder 0)(has-subtarget? Lst SubA SubB '()))
      ((not(null? Lst)) ;do recursion?
         (begin
           (has-subtarget? (cdr Lst) (+ SubA (car Lst)) SubB Holder)
           (has-subtarget? (cdr Lst) SubA (+ SubB (car Lst)) Holder)
           (has-subtarget? (cdr Lst) SubA SubB (append Holder (list(car Lst))))))
      ((and(not(null? Holder))(and(not(null? SubA))(= SubA SubB))) ;testable?
         (has-target-num? SubA Holder))
      ))