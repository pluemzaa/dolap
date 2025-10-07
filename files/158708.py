<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3586;&#3657;&#3629;4"/>
        <attribute name="authors" value="windows"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 09:13:03 PM"/>
        <attribute name="created" value="d2luZG93cztMQVBUT1AtNUZDME03VlU7MjU2OC0wNy0yMjswODozMzowNCBQTTszMTIz"/>
        <attribute name="edited" value="d2luZG93cztMQVBUT1AtNUZDME03VlU7MjU2OC0wNy0yMjswOToxMzowMyBQTTs2OzMyMzQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="1"/>
            <while expression="i&lt;=years">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;Year&quot;&amp;i&amp;&quot;:&quot;&amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>