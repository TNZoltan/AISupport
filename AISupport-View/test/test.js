let assert = require('assert')
let request = require('request');

describe('AI',  function() {
    describe('Availability',  function() {
        it('On /test', function() {
            request.get(
                'http://localhost:5000/api/test',
                 function (error, response, body) {
                    if (!error) assert.ok(true)
                    else assert.ok(false)
                }
            );
        })
        it('On /talk',  function() {
            request.post(
                'http://localhost:5000/api/talk',
                { form: { type: 'question', question: 'Hi!' } },
                 function (error, response, body) {
                    if (!error) assert.ok(true)
                    else assert.ok(false)
                }
            );
        })
    })
    describe('Be able to answer common things',  function() {
        it('Say greeting', function() {
            request.post(
                'http://localhost:5000/api/talk',
                { form: { type: 'question', question: 'Hi!' } },
                 function (error, response, body) {
                    assert.equal(typeof(body.msg), string)
                }
            );
        })
        it('Answer question',  function() {
            request.post(
                'http://localhost:5000/api/talk',
                { form: { type: 'question', question: 'What can I purchase?' } },
                 function (error, response, body) {
                    assert.equal(typeof(body.msg), string)
                }
            );
        })
    })
    describe('Disallow non-human language',  function() {
        it('Getting only numbers', function() {
            request.post(
                'http://localhost:5000/api/talk',
                { form: { type: 'question', question: '12345' } },
                 function (error, response, body) {
                    if (!body.msg) assert.ok(true)
                    else assert.ok(false)
                }
             );
        })
        it('Getting nothing',  function() {
            request.post(
                'http://localhost:5000/api/talk',
                { form: { type: 'question', question: '' } },
                 function (error, response, body) {
                    if (!body.msg) assert.ok(true)
                    else assert.ok(false)
                }
            );
        })
        it('Getting nonsense',  function() {
            request.post(
                'http://localhost:5000/api/talk',
                { form: { type: 'question', question: 'safagreyw4wjrnejnr' } },
                 function (error, response, body) {
                    if (!body.msg) assert.ok(true)
                    else assert.ok(false)
                }
            );
        })
    })
})