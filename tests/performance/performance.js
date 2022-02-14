import http from 'k6/http';
import { sleep, check } from 'k6';
import { jUnit, textSummary } from 'https://jslib.k6.io/k6-summary/0.0.1/index.js';

export const options = {
    duration: '1m',
    vus: 5,
    thresholds: {
        http_req_duration: ['p(95)<500']
    },
};
export default function () {
    let urlString = __ENV.API_ENDPOINT.replace(/["]+/g, '');
    let res = http.get(`${urlString}/test/getHello?lang=en`, { tags: { name: '01_Home' } });
    check(res, {
        'is status 200': (r) => r.status === 200,
        'text verification': (r) => r.body.includes("Hello World")
    });
    sleep(Math.random() * 5);
}
export function handleSummary(data) {
    return {
        'stdout': textSummary(data, { indent: ' ', enableColors: true }),
        './TESTS-loadtest-results.xml': jUnit(data),
    }
}