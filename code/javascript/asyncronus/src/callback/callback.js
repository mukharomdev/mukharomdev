export function Callback(param1,param2,callback){
  let result = param1 + param2

  if(typeof callback == 'function'){
  	result = callback(param1,param2)
  }
  	return result
}


export function ArgumentCallback(x,y){
	return  "(ini baris callback) jumlahnya sama dengan " + `${ x + y}`
}