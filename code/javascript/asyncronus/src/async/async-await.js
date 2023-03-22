export async function AsyncAwait(param){
	
	let result;
	let value = 100;

	if(typeof param == 'function'){
		result = await param(value)
		
		console.log("contoh async await\n",result,"\nend async await")
		
	}
	
    
    
}