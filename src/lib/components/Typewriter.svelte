<script lang="ts">
    export let messages: string[] = [];
    export let delay: number = 50;
    export let pauseDelay: number = 1000;
    export let cycleDelay: number = 3000;

    let displayText = '';
    let currentMessageIndex = 0;
    let currentCharIndex = 0;
    let isTyping = true;
    let isPausing = false;

    function typeNextChar() {
        const currentMessage = messages[currentMessageIndex];

        if (currentCharIndex < currentMessage.length) {
            displayText = currentMessage.slice(0, currentCharIndex + 1);
            currentCharIndex++;
            setTimeout(typeNextChar, delay);
        } else {
            isTyping = false;
            isPausing = true;
            setTimeout(() => {
                if (currentMessageIndex === messages.length - 1) {
                    // If we've completed a full cycle, use the longer cycleDelay
                    setTimeout(() => {
                        currentMessageIndex = 0;
                        currentCharIndex = 0;
                        isTyping = true;
                        isPausing = false;
                        displayText = '';
                        typeNextChar();
                    }, cycleDelay);
                } else {
                    currentMessageIndex++;
                    currentCharIndex = 0;
                    isTyping = true;
                    isPausing = false;
                    displayText = '';
                    typeNextChar();
                }
            }, pauseDelay);
        }
    }

    typeNextChar();
</script>

<h1 class="text-4xl font-bold mb-20">
    {#if displayText.length > 0}
        {displayText.slice(0, -1)}<span class="last-char">{displayText.slice(-1)}</span>
    {/if}
    {#if isTyping}
        <span class="animate-blink">|</span>
    {/if}
</h1>

<style>
    @keyframes blink {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
    }

    .animate-blink {
        animation: blink 0.7s infinite;
    }

    .last-char {
        font-weight: bold;
        color: #6fb8f5;
    }
</style>