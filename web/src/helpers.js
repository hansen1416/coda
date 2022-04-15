import axios from "axios";

export function http_request(method, path, callback, component, data) {
	const param = {
		method: method,
		url: import.meta.env.VITE_API_URL + path,
	};

	if (data) {
		param["data"] = data;
	}

	const jwt = localStorage.getItem("jwt");

	if (jwt) {
		param["headers"] = { Authorization: "Bearer " + jwt };
	}

	axios.request(param).then((response) => {
		if (response.data) {
			if (response.data.error) {
				component.error = response.data.error;

				setTimeout(() => {
					component.error = "";
				}, 5000);
			} else {
				callback(response.data);
			}
		} else {
			component.error = "wrong response format";

			setTimeout(() => {
				component.error = "";
			}, 5000);
		}
	});
}
