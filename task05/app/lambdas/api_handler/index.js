const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();


exports.handler = async (event) => {
	
	const item = {
        TableName: 'Events',
        Item: {
            id: "ID_TEST", 
            data: "TEST"
        },
    };

	await dynamoDB.put(item).promise();
    
	const response = {
        statusCode: 201,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
