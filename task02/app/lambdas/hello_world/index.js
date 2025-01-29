exports.handler = async (event) => {
    if(path == "/hello" && httpMethod == "GET"){
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
	}
};
