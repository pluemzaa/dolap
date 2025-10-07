<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test3_lap4"/>
        <attribute name="authors" value="NATNICHA-PC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 06:35:18 PM"/>
        <attribute name="created" value="TkFUTklDSEEtUEM7TkFUTklDSEE7MjAyNS0wNy0yMTswNTo1OToyNSBQTTsyNjQ1"/>
        <attribute name="edited" value="TkFUTklDSEEtUEM7TkFUTklDSEE7MjAyNS0wNy0yMTswNjozNToxOCBQTTs1OzI3NTQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, newMoney" type="Real" array="False" size=""/>
            <declare name="years, year" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;input years:&quot;" newline="True"/>
            <input variable="years"/>
            <for variable="year" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot; &amp; year &amp;&quot;: &quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>