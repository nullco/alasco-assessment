class Ajax {

    static send(request, callback) {

        const serializers = {
            'application/json': (data) => {
                return JSON.stringify(data);
            }
        }

        const deserializers = {
            'application/json': (text) => {
                return JSON.parse(text);
            }
        }

        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4) {
                const contentType = this.getResponseHeader('Content-Type').split('; ')[0];
                let response = this.responseText;
                if (contentType in deserializers) {
                    const deserializer = deserializers[contentType];
                    response = deserializer(response);
                }
                callback(response);
            }
        };
        xhttp.open(request.type, request.url, true);

        let serializer = null;
        if (request.headers) {
            let headers = request.headers;
            for (let header of headers) {
                const key = header[0];
                const value = header[1];
                if (key == 'Content-Type') {
                    serializer = serializers[value];
                }
                xhttp.setRequestHeader(key, value);
            }
        }
        if (request.data) {
            let data = request.data;
            if (serializer) {
                data = serializer(data);
            }
            xhttp.send(data);
        } else {
            xhttp.send();
        }
    }
}


class CurrencyConverter {

    constructor() {
        this.sourceCurrencySelect = document.getElementById("source-currency");
        this.sourceAmount = document.getElementById("source-amount");
        this.targetCurrencySelect = document.getElementById("target-currency");
        this.targetAmount = document.getElementById("target-amount");
        this.currencies = [];
        this.loadCurrencies();
    }

    loadCurrencies() {
        Ajax.send({
            type: "GET",
            url: "/api/currencies"
        }, (response) => {
            this.currencies = response.results;
            this.init();
        });
    }

    init() {
        this.initSelect(this.sourceCurrencySelect);
        this.initSelect(this.targetCurrencySelect);
        this.initInput();
        this.convert();
    }

    initSelect(select) {
        let other = null;
        let initialValue = null;
        if (select == this.sourceCurrencySelect) {
            initialValue = this.currencies[0]._id;
            other = this.targetCurrencySelect;
        } else {
            initialValue = this.currencies[1]._id;
            other = this.sourceCurrencySelect;
        }
        select.innerHTML = "";
        for (let currency of this.currencies) {
            let option = document.createElement("option");
            option.value = currency._id;
            option.text = currency.name + " (" + currency._id + ")";
            select.add(option);
        }
        select.value = initialValue;
        let previousValue = select.value;
        select.addEventListener("change", () => {
            if (select.value == other.value) {
                other.value = previousValue;
            }
            previousValue = select.value;
            this.convert();
        });
    }

    initInput() {
        this.sourceAmount.value = 1.0;
        this.sourceAmount.addEventListener("input", () => {
            this.convert()
        });
    }

    convert() {
        if (!this.sourceAmount.value) {
            return;
        }
        const sourceCurrency = this.sourceCurrencySelect.value;
        const amount = parseFloat(this.sourceAmount.value)
        const targetCurrency = this.targetCurrencySelect.value;

        Ajax.send({
            type: "POST",
            url: `/api/currencies/${sourceCurrency}/to/${targetCurrency}`,
            data: {
                'amount': amount
            },
            headers: [
                ['Content-Type', 'application/json']    
            ]
        }, (response) => {
            let amount = response.amount;
            this.targetAmount.value = amount;
        });
    }

}


new CurrencyConverter();