export function promise(param){
	
	let promisify = new Promise((resolve,reject)=>{

		if(typeof param == 'number'){
			resolve(param)
		}else{
			throw new Error("bukan angka")
		}
	})
	return promisify;
}