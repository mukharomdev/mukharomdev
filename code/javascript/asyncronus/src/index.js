import {promise} from './promise/promise.js'
import {Blocking} from './blocking/blocking.js'
import {AsyncAwait} from './async/async-await.js'
import {Callback,ArgumentCallback} from './callback/callback.js'

// deklaration main
function main(){
    
	let promis = promise(3);
	promis
		  .then(num =>num)
		  .then(result=>{
		  	console.log("contoh promise\n")
		  	console.log(result)
		  	return result + 10;
		  })
		  .then(result2=>console.log(result2,"\nend promise"))
		  .catch(error=>console.log(error));

    
    Blocking(1)
    AsyncAwait(promise)

    let callback = Callback(3,3,ArgumentCallback)
    console.log(callback)

   
   

}



// execute main
// 
main();