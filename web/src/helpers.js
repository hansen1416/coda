import axios from "axios";

export const permission_owner = 1;
export const permission_admin = 2;
export const permission_mod = 3;

export function http_request(method, path, callback, component, data, headers) {
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

	if (headers) {
		param["headers"] = headers;
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
