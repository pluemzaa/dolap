<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lap4"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 01:31:30 AM"/>
        <attribute name="created" value="TGVub3ZvO0RFU0tUT1AtTFRVR0FETjsyNTY4LTA3LTE2OzExOjU3OjMzIFBNOzMwMzY="/>
        <attribute name="edited" value="TGVub3ZvO0RFU0tUT1AtTFRVR0FETjsyNTY4LTA3LTE3OzAxOjMxOjMwIEFNOzU7MzEyMg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; years">
                <assign variable="i" expression="i+1"/>
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot;&amp; i &amp; &quot;: &quot;&amp; money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>