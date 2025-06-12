import React, { useEffect, useRef } from 'react';

export default function PaypalButton({ amount, onSuccess }) {
  const paypalRef = useRef();

  useEffect(() => {
    const CLIENT_ID = process.env.REACT_APP_PAYPAL_CLIENT_ID || 'sb';

    const addPayPalScript = async () => {
      const script = document.createElement('script');
      script.type = 'text/javascript';
      script.src = `https://www.paypal.com/sdk/js?client-id=${CLIENT_ID}`;
      script.async = true;
      script.onload = () => {
        window.paypal
          .Buttons({
            createOrder: (data, actions) => {
              return actions.order.create({
                purchase_units: [
                  {
                    amount: {
                      value: amount,
                    },
                  },
                ],
              });
            },
            onApprove: (data, actions) => {
              return actions.order.capture().then((details) => {
                onSuccess(details);
              });
            },
          })
          .render(paypalRef.current);
      };
      document.body.appendChild(script);
    };

    addPayPalScript();
  }, [amount, onSuccess]);

  return <div ref={paypalRef}></div>;
}
