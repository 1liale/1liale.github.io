<script lang="ts">
import {
    Timeline,
    TimelineItem,
    TimelineSeparator,
    TimelineDot,
    TimelineConnector,
    TimelineContent,
    TimelineOppositeContent
} from 'svelte-vertical-timeline';
import Saos from "saos";

export let timelineData: { period: string; title: string; company: string; description: string; techStack: string[] }[];
</script>

<Timeline position="alternate">
    {#each timelineData as item, index}
        <TimelineItem>
            <TimelineOppositeContent slot="opposite-content">
                <span class="text-sm text-gray-600 dark:text-gray-400">{item.period}</span>
            </TimelineOppositeContent>
            <TimelineSeparator>
                <TimelineDot style="background-color: #6fb8f5;" />
                {#if index < timelineData.length - 1}
                    <TimelineConnector style="background-color: #6fb8f5;" />
                {/if}
            </TimelineSeparator>
            <TimelineContent>
                <Saos animation={"fade-in 1.2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both"}>
                    <div class="timeline-item-content text-left">
                        <h4 class="text-xl font-semibold">{item.title}</h4>
                        <p class="text-gray-400">{item.company}</p>
                        {#each item.description.split('\n') as line}
                            <p class="mt-2">{line}</p>
                        {/each}
                        <div class="tech-stack">
                            {#each item.techStack as tech}
                                <span class="tech-item">{tech}</span>
                            {/each}
                        </div>
                    </div>
                </Saos>
            </TimelineContent>
        </TimelineItem>
    {/each}
</Timeline>

<style>
    .timeline-item-content {
        padding: 20px;
        border: 2px solid #385a9088;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        color: #e5e7eb;
    }

    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }

    .tech-item {
        background-color: #4b5563;
        color: #e5e7eb;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.875rem;
    }

    @keyframes -global-fade-in {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
</style>
