exports.handler = async (event) => {
	
	const path = event.path
	
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!' + path),
    };
    return response;
};
