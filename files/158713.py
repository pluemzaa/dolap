<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="l4"/>
        <attribute name="authors" value="atc"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 09:14:06 PM"/>
        <attribute name="created" value="YXRjO0RFU0tUT1AtT0U0TzJCVjsyMDI1LTA3LTIyOzA4OjM0OjMwIFBNOzI2NTg="/>
        <attribute name="edited" value="YXRjO0RFU0tUT1AtT0U0TzJCVjsyMDI1LTA3LTIyOzA5OjE0OjA2IFBNOzQ7Mjc3MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, sum, i, sums" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <assign variable="interest" expression="interest/100"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="0"/>
            <while expression="i&lt;years">
                <assign variable="i" expression="i+1"/>
                <assign variable="sum" expression="money*interest"/>
                <assign variable="sums" expression="money + sum"/>
                <output expression="&quot;Year &quot;&amp; i &amp;&quot;: &quot;&amp; sums" newline="True"/>
                <assign variable="money" expression="money + sum"/>
            </while>
        </body>
    </function>
</flowgorithm>