<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="1234576890"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:39:01 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjo0MjowMyBQTTsyNTQw"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozOTowMSBQTTs0OzI2NTY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Baht" type="Real" array="False" size=""/>
            <declare name="year, i, intrest, tureintrest" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="Baht"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="intrest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="tureintrest" expression="intrest / 100"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="Baht" expression="Baht * (1 + (intrest / 100))"/>
                <assign variable="i" expression="i + 1"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; Baht" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>