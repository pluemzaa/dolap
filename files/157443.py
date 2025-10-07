<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lap4_4"/>
        <attribute name="authors" value="sooth"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 11:49:56 AM"/>
        <attribute name="created" value="c29vdGg7QU9NU0lOTjsyMDI1LTA3LTE5OzExOjIxOjQxIEFNOzIzNTU="/>
        <attribute name="edited" value="c29vdGg7QU9NU0lOTjsyMDI1LTA3LTE5OzExOjQ5OjU2IEFNOzI7MjQ4MA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="years, interest, totalyears" type="Integer" array="False" size=""/>
            <assign variable="years" expression="1"/>
            <declare name="afterinterest, money, money1, money2, money3, amount" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <assign variable="amount" expression="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="totalyears"/>
            <while expression="years&lt;=totalyears">
                <assign variable="amount" expression="amount+(amount*(interest/100))"/>
                <output expression="&quot;Year&quot;&amp;years&amp;&quot;:&quot;&amp;amount" newline="True"/>
                <assign variable="years" expression="years+1"/>
            </while>
        </body>
    </function>
</flowgorithm>