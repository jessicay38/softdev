(define fact
  (lambda (n)
    (if (= n 1)
        1
        (* n (fact(- n 1))))))

(define fib
  (lambda (n)
    (cond ((= n 0) 1)
          ((= n 1) 1)
          (else (+ (fib (- n 1))
                (+ (fib (- n 2))))))))     

