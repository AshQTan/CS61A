(define (find s predicate)
  (cond
  	((null? s) '#f)
  	((predicate (car s)) (car s))
  	(else (find (cdr-stream s) predicate))
  	)
)

(define (scale-stream s k)
  ;(stream-map (lambda (x) (* x k)) s)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))


)

(define (has-cycle s)
	(define (helper sless)
	  (cond
	  	((null? sless) False)
	  	((eq? (cdr-stream sless) s) True)
	  	(else (helper (cdr-stream sless) ))
	  	)		
		)
	(helper s)



)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
