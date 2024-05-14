import React, { useEffect, useRef } from 'react';
import { DataSet, Network } from 'vis-network/standalone/esm/vis-network';

const MindMap = ({ data }) => {
    const domNode = useRef(null);

    useEffect(() => {
        if (!data) return;

        const nodes = new DataSet([
            { id: 1, label: data.main_topic, color: '#f0a30a', shape: 'ellipse', size: 30 },
            ...data.subtopics.map((subtopic, index) => ({
                id: index + 2,
                label: subtopic,
                color: '#7cbb00',
                shape: 'box',
                size: 25
            }))
        ]);

        const edges = data.subtopics.map((subtopic, index) => ({
            from: 1,
            to: index + 2,
            arrows: 'to'
        }));

        const options = {
            nodes: {
                borderWidth: 2,
                borderWidthSelected: 4,
                font: { size: 16 }
            },
            edges: {
                color: 'lightgray',
                smooth: true
            },
            layout: {
                hierarchical: {
                    direction: "UD",
                    sortMethod: "directed",
                    levelSeparation: 150,
                    nodeSpacing: 150
                }
            },
            physics: false,
            interaction: { hover: true }
        };

        const network = new Network(domNode.current, { nodes, edges }, options);

        return () => {
            network.destroy();
        };
    }, [data]);

    return <div ref={domNode} style={{ height: '800px', width: '100%' }} />;
};


export default MindMap;
