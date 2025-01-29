exports.handler = async (event) => {
    //const path = event.path;
	//const httpMethod = event.httpMethod;
	
	return {
		statusCode: 200,
		body: JSON.stringify({statusCode: 200, message: "Hello from Lambda"}),
	}
	
	/*if(path == "/hello" && httpMethod == "GET"){
		return {
			statusCode: 200,
			body: JSON.stringify({message: "Hello from Lambda"}),
		}
	}
	else{
		return {
			statusCode: 400,
			body: JSON.stringify({message: "Bad request syntax or unsupported method. Request path: " + path + ". HTTP method: " + httpMethod}),
		}
	}*/
};
