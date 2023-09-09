async function requestData(api, data) {
    return fetch(api, {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(data)
    })
}

async function recieveData(response, extr) {
    try {
        if (!response.ok) {fire(await response.text()); return false}
        return extr(response)
    } catch (ex) {return false}
}

function extractImg(response) {return response.blob()}

function extractJSON(response) {return response.json()}

