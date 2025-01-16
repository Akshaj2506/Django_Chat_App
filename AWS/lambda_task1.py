def lambda_handler(event, context):
    try:
        num1 = event.get('num1')
        num2 = event.get('num2')

        if num1 is None or num2 is None:
            return {
                'statusCode': 400,
                'body': 'Missing parameters: num1 and num2 are required.'
            }

        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return {
                'statusCode': 400,
                'body': 'Invalid input: num1 and num2 must be numbers.'
            }

        result = num1 + num2

        return {
            'statusCode': 200,
            'body': {
                'num1': num1,
                'num2': num2,
                'result': result
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
