import { defineComponent, h, PropType } from 'vue'

import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Plugin
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
)

export default defineComponent({
  name: 'LineChart',
  components: {
    Line
  },
  props: {
    chartId: {
      type: String,
      default: 'line-chart'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    }
  },
  setup(props) {

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          stacked: true,
          title: {
            display: true,
            text: 'AGE'
          }
        },
        y: {
          stacked: true,
          max:100,
          min:0,
          ticks: {
            beginAtZero: true,
            stepSize: 1,
          },
          title: {
            display: true,
            text: 'Cancer risk (%)'
          }
          
        }
      },
      plugins: {
        // legend: {
        //   position:'bottom'
        // },
        datalabels: {
          formatter: function(value) {
            if(isNaN(value)){
              return 0;
            }
            return Math.round(value*10)/10;
          }
        },
      }
    }

    return () =>
      h(Line, {
        chartOptions,
        chartId: props.chartId,
        width: props.width,
        height: props.height,
        cssClasses: props.cssClasses,
        styles: props.styles,
        plugins: props.plugins
      })
  }
})