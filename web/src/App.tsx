import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import 'chart.js/auto';

interface Data {
  name: string;
  salary: number;
  mean_salary: number;
}

const App: React.FC = () => {
  const [data, setData] = useState<Data[]>([]);

  useEffect(() => {
    fetch('/api/data')
      .then((response) => response.json())
      .then((data) => setData(JSON.parse(data)));
  }, []);

  const chartData = {
    labels: data.map((item) => item.name),
    datasets: [
      {
        label: 'Salary',
        data: data.map((item) => item.salary),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  return (
    <div>
      <h1>Data Visualization</h1>
      <Bar data={chartData} />
    </div>
  );
};

export default App;
