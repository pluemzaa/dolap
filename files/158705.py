<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3586;&#3657;&#3629;3"/>
        <attribute name="authors" value="windows"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 08:30:34 PM"/>
        <attribute name="created" value="d2luZG93cztMQVBUT1AtNUZDME03VlU7MjU2OC0wNy0yMjswODoxMDoyNCBQTTszMTIw"/>
        <attribute name="edited" value="d2luZG93cztMQVBUT1AtNUZDME03VlU7MjU2OC0wNy0yMjswODozMDozNCBQTTsxOzMyMzE="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="numstart, numend, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="numstart"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="numend"/>
            <assign variable="i" expression="numstart"/>
            <while expression="i&lt;=numend">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>